from photonicdrivers.Attocube_ASC500.FilesFromAttocubeGit.lib import ASC500
from photonicdrivers.Attocube_ASC500.FilesFromAttocubeGit.lib.asc500_scanner import ASC500Scanner
import os

# has to run on the attocube PC

binPath = "C:\\gitRepositories\\NQCP-Phot-Git-Drivers\\photonicdrivers\\Attocube_ASC500\\FilesFromAttocubeGit\\Installer\\ASC500CL-V2.7.13\\"
dllPath = "C:\\gitRepositories\\NQCP-Phot-Git-Drivers\\photonicdrivers\\Attocube_ASC500\\FilesFromAttocubeGit\\64bit_lib\\ASC500CL-LIB-WIN64-V2.7.13\\daisybase\\lib\\"
dll_loc = dllPath + 'daisybase.dll'

print(os.path.isfile(dll_loc))

asc500 = ASC500(binPath, dllPath)
# asc500 = ASC500Scanner(binPath, dllPath)
