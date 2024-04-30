import numpy as np
import win32gui, win32ui, win32con


class WindowCapture:

    # properties


    # constructor
    def __init__(self, window_name=None):
        self.window_name = window_name

    def get_screenshot(self):
        if self.window_name is None:
            hwnd = win32gui.GetDesktopWindow()
        else:
            hwnd = win32gui.FindWindow(None, self.window_name)
            if not hwnd:
                raise Exception('Window not found: {}'.format(self.window_name))

        window_rectangle = win32gui.GetWindowRect(hwnd)
        window_width = window_rectangle[2] - window_rectangle[0]
        window_height = window_rectangle[3] - window_rectangle[1]

        # account for the window border and titlebar and cut them off
        num_left_border_pixels = 53
        num_upper_pixels = 90
        num_right_border_pixels = 16
        num_lower_pixels = 408


        screen_shot_window_width = window_width - num_right_border_pixels - num_left_border_pixels
        screen_shot_window_height = window_height - num_upper_pixels - num_lower_pixels

        # get the window image data
        wDC = win32gui.GetWindowDC(hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj,  screen_shot_window_width, screen_shot_window_height)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (window_width, window_height), dcObj, ( num_left_border_pixels, num_upper_pixels), win32con.SRCCOPY)

        # convert the raw data into a format opencv can read
        #dataBitMap.SaveBitmapFile(cDC, 'debug.bmp')
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (screen_shot_window_height, screen_shot_window_width, 4)

        # free resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        # drop the alpha channel, or cv.matchTemplate() will throw an error like:
        #   error: (-215:Assertion failed) (depth == CV_8U || depth == CV_32F) && type == _templ.type() 
        #   && _img.dims() <= 2 in function 'cv::matchTemplate'
        img = img[...,:3]

        # make image C_CONTIGUOUS to avoid errors that look like:
        #   File ... in draw_rectangles
        #   TypeError: an integer is required (got type tuple)
        # see the discussion here:
        # https://github.com/opencv/opencv/issues/14866#issuecomment-580207109
        img = np.ascontiguousarray(img)

        return img

    # find the name of the window you're interested in.
    # once you have it, update window_capture()
    # https://stackoverflow.com/questions/55547940/how-to-get-a-list-of-the-name-of-every-open-window
    @staticmethod
    def list_window_names():
        def winEnumHandler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                print(hex(hwnd), win32gui.GetWindowText(hwnd))
        win32gui.EnumWindows(winEnumHandler, None)

    # translate a pixel position on a screenshot image to a pixel position on the screen.
    # pos = (x, y)
    # WARNING: if you move the window being captured after execution is started, this will
    # return incorrect coordinates, because the window position is only calculated in
    # the __init__ constructor.
    def get_screen_position(self, pos):
        return (pos[0] + self.screen_shot_left, pos[1] + self.screen_shot_upper)
