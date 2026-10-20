namespace LabBrickAttTest
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.numericUpDown1 = new System.Windows.Forms.NumericUpDown();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.label3 = new System.Windows.Forms.Label();
            this.NumberOfDevices = new System.Windows.Forms.Label();
            this.Dll_Version = new System.Windows.Forms.Label();
            this.button1 = new System.Windows.Forms.Button();
            this.button2 = new System.Windows.Forms.Button();
            this.label4 = new System.Windows.Forms.Label();
            this.Max_Atten_Label = new System.Windows.Forms.Label();
            this.Chnllbl = new System.Windows.Forms.Label();
            this.Chnlupdown = new System.Windows.Forms.NumericUpDown();
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown1)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.Chnlupdown)).BeginInit();
            this.SuspendLayout();
            // 
            // numericUpDown1
            // 
            this.numericUpDown1.DecimalPlaces = 1;
            this.numericUpDown1.Increment = new decimal(new int[] {
            1,
            0,
            0,
            65536});
            this.numericUpDown1.Location = new System.Drawing.Point(27, 90);
            this.numericUpDown1.Margin = new System.Windows.Forms.Padding(2, 2, 2, 2);
            this.numericUpDown1.Maximum = new decimal(new int[] {
            120,
            0,
            0,
            0});
            this.numericUpDown1.Name = "numericUpDown1";
            this.numericUpDown1.Size = new System.Drawing.Size(90, 20);
            this.numericUpDown1.TabIndex = 0;
            this.numericUpDown1.ValueChanged += new System.EventHandler(this.numericUpDown1_ValueChanged);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(25, 65);
            this.label1.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(87, 13);
            this.label1.TabIndex = 1;
            this.label1.Text = "Attenuation in db";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(25, 195);
            this.label2.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(65, 13);
            this.label2.TabIndex = 2;
            this.label2.Text = "LDA Name: ";
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(25, 161);
            this.label3.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(134, 13);
            this.label3.TabIndex = 3;
            this.label3.Text = "Number of Devices Found:";
            // 
            // NumberOfDevices
            // 
            this.NumberOfDevices.AutoSize = true;
            this.NumberOfDevices.Location = new System.Drawing.Point(158, 161);
            this.NumberOfDevices.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.NumberOfDevices.Name = "NumberOfDevices";
            this.NumberOfDevices.Size = new System.Drawing.Size(13, 13);
            this.NumberOfDevices.TabIndex = 4;
            this.NumberOfDevices.Text = "0";
            // 
            // Dll_Version
            // 
            this.Dll_Version.AutoSize = true;
            this.Dll_Version.Location = new System.Drawing.Point(25, 258);
            this.Dll_Version.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.Dll_Version.Name = "Dll_Version";
            this.Dll_Version.Size = new System.Drawing.Size(68, 13);
            this.Dll_Version.TabIndex = 5;
            this.Dll_Version.Text = "DLL Version ";
            // 
            // button1
            // 
            this.button1.Location = new System.Drawing.Point(27, 124);
            this.button1.Margin = new System.Windows.Forms.Padding(2, 2, 2, 2);
            this.button1.Name = "button1";
            this.button1.Size = new System.Drawing.Size(108, 26);
            this.button1.TabIndex = 6;
            this.button1.Text = "Find LDA Device";
            this.button1.UseVisualStyleBackColor = true;
            this.button1.Click += new System.EventHandler(this.button1_Click);
            // 
            // button2
            // 
            this.button2.Location = new System.Drawing.Point(160, 124);
            this.button2.Margin = new System.Windows.Forms.Padding(2, 2, 2, 2);
            this.button2.Name = "button2";
            this.button2.Size = new System.Drawing.Size(102, 26);
            this.button2.TabIndex = 7;
            this.button2.Text = "Close LDA Device";
            this.button2.UseVisualStyleBackColor = true;
            this.button2.Click += new System.EventHandler(this.button2_Click);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.8F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label4.Location = new System.Drawing.Point(24, 17);
            this.label4.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(225, 18);
            this.label4.TabIndex = 8;
            this.label4.Text = "Vaunix LDA C# example program";
            // 
            // Max_Atten_Label
            // 
            this.Max_Atten_Label.AutoSize = true;
            this.Max_Atten_Label.Location = new System.Drawing.Point(25, 227);
            this.Max_Atten_Label.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.Max_Atten_Label.Name = "Max_Atten_Label";
            this.Max_Atten_Label.Size = new System.Drawing.Size(111, 13);
            this.Max_Atten_Label.TabIndex = 9;
            this.Max_Atten_Label.Text = "Maximum Attenuation:";
            // 
            // Chnllbl
            // 
            this.Chnllbl.AutoSize = true;
            this.Chnllbl.Location = new System.Drawing.Point(140, 65);
            this.Chnllbl.Margin = new System.Windows.Forms.Padding(2, 0, 2, 0);
            this.Chnllbl.Name = "Chnllbl";
            this.Chnllbl.Size = new System.Drawing.Size(46, 13);
            this.Chnllbl.TabIndex = 10;
            this.Chnllbl.Text = "Channel";
            // 
            // Chnlupdown
            // 
            this.Chnlupdown.Location = new System.Drawing.Point(143, 90);
            this.Chnlupdown.Margin = new System.Windows.Forms.Padding(2);
            this.Chnlupdown.Maximum = new decimal(new int[] {
            4,
            0,
            0,
            0});
            this.Chnlupdown.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.Chnlupdown.Name = "Chnlupdown";
            this.Chnlupdown.Size = new System.Drawing.Size(90, 20);
            this.Chnlupdown.TabIndex = 11;
            this.Chnlupdown.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
            this.Chnlupdown.ValueChanged += new System.EventHandler(this.Chnlupdown_ValueChanged);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(525, 375);
            this.Controls.Add(this.Chnlupdown);
            this.Controls.Add(this.Chnllbl);
            this.Controls.Add(this.Max_Atten_Label);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.button2);
            this.Controls.Add(this.button1);
            this.Controls.Add(this.Dll_Version);
            this.Controls.Add(this.NumberOfDevices);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.numericUpDown1);
            this.Margin = new System.Windows.Forms.Padding(2, 2, 2, 2);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.numericUpDown1)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.Chnlupdown)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.NumericUpDown numericUpDown1;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Label NumberOfDevices;
        private System.Windows.Forms.Label Dll_Version;
        private System.Windows.Forms.Button button1;
        private System.Windows.Forms.Button button2;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label Max_Atten_Label;
        private System.Windows.Forms.Label Chnllbl;
        private System.Windows.Forms.NumericUpDown Chnlupdown;
    }
}

