// Vaunix example program
// Calling the LDA DLL from a C# program
// Updated by NJB 3/6/2026
// This example uses the 64 bit LDA DLL
// It is intended to show how to call the API, and is a very basic example of using the API
// The example does not include the kind of error handling that would be present in a production application
// It also does not implement the kind of classes which might be used in an actual application
// This example shows the use of the newer "HR" functions which specify attenuation in .05 db units.
//
// This example shows both accessing the LDA API functions directly, by LabBrickWrapper.FunctionName
// and also using wrapper functions in the LabBrickWrapper class. Typically it would be a better design to
// choose one approach for an application, not mix the two approaches. I am showing both approaches here
// as examples of API access, not overall application architecture.
// 



using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;
using System.Globalization;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace LabBrickAttTest
{
    public partial class Form1 : Form
    {
        private int m_NumberOfDevices = 0;
        LabBrickWrapper m_LabBrick = null;

        private int m_dllversion = 0;
        private bool LDA_Open = false;

        public Form1()
        {
            InitializeComponent();

            m_LabBrick = new LabBrickWrapper();

            // show our DLL version
            m_dllversion = m_LabBrick.GetDLLVersion();
            Dll_Version.Text = "DLL Version " + m_dllversion.ToString("X3", CultureInfo.CurrentCulture); 


            // Set test mode false to look for actual hardware
            m_LabBrick.SetTestMode(false);

        }

        private void numericUpDown1_ValueChanged(object sender, EventArgs e)
        {
            float tmp_attenuation = 0;

            if (LDA_Open)
            {
                tmp_attenuation = (float)numericUpDown1.Value;
                m_LabBrick.SetAttenuationInDb(m_LabBrick.MyDevices[0], tmp_attenuation);
            }
        }

        // search for devices and open the first one we find
        private void button1_Click(object sender, EventArgs e)
        {
            int status = 0;
            int testattval = 0;
            byte[] temp = new byte[32];
            float ftemp = 0;
            int numchan = 1;

            m_NumberOfDevices = m_LabBrick.GetNumberOfDevices();    // How many devices did we find?
            NumberOfDevices.Text = m_NumberOfDevices.ToString();

            if (m_NumberOfDevices > 0 && !LDA_Open)
            {
                status = m_LabBrick.GetDevices();

                status = m_LabBrick.InitDevice(m_LabBrick.MyDevices[0]);    // we will just use the first device
                LDA_Open = true;

                // lets show the name of the device
                status = m_LabBrick.GetModelNameA(m_LabBrick.MyDevices[0], temp);

                string LDA_Name = Encoding.UTF8.GetString(temp, 0, temp.Length);
                label2.Text = LDA_Name;

                // Set the device to channel 1
                Chnlupdown.Value = 1;

                status = m_LabBrick.SetChannel(m_LabBrick.MyDevices[0], 1);

                // Get the number of channels
                numchan = LabBrickWrapper.fnLDA_GetNumChannels(m_LabBrick.MyDevices[0]);
                Chnlupdown.Maximum = numchan;

                // get some parameters about the device
                status = LabBrickWrapper.fnLDA_GetMaxAttenuationHR(m_LabBrick.MyDevices[0]);
                if (status >= 0)
                {
                    ftemp = (float)status / 20.0F;
                    Max_Atten_Label.Text = "Maximum Attenuation: " + ftemp.ToString("F2", CultureInfo.CurrentCulture) + " dB";
                }
                else
                {
                    // Do something about the error.
                }

                testattval = m_LabBrick.GetAttenuationHR(m_LabBrick.MyDevices[0]);

                // initialize our attenuation control with the existing device setting
                numericUpDown1.Value = (decimal) m_LabBrick.GetAttenuationHR(m_LabBrick.MyDevices[0]) / 20M;

            }
        }

        private void button2_Click(object sender, EventArgs e)
        {
            if (LDA_Open)
            {
                m_LabBrick.CloseDevice(m_LabBrick.MyDevices[0]);
                LDA_Open = false;
            }
        }

        private void Chnlupdown_ValueChanged(object sender, EventArgs e)
        {
            int tmp_chnl = 1;

            if (LDA_Open)
            {
                tmp_chnl = (int)Chnlupdown.Value;
                m_LabBrick.SetChannel(m_LabBrick.MyDevices[0], tmp_chnl);

                // initialize our attenuation control with the existing device setting
                numericUpDown1.Value = (decimal)m_LabBrick.GetAttenuationHR(m_LabBrick.MyDevices[0]) / 20M;

            }
        }
    }
}
