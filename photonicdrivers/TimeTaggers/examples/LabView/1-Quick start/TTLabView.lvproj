<?xml version='1.0' encoding='UTF-8'?>
<Project Type="Project" LVVersion="14008000">
	<Property Name="NI.LV.All.SourceOnly" Type="Bool">true</Property>
	<Property Name="NI.Project.Description" Type="Str"></Property>
	<Item Name="My Computer" Type="My Computer">
		<Property Name="server.app.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.control.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="server.tcp.enabled" Type="Bool">false</Property>
		<Property Name="server.tcp.port" Type="Int">0</Property>
		<Property Name="server.tcp.serviceName" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.tcp.serviceName.default" Type="Str">My Computer/VI Server</Property>
		<Property Name="server.vi.callsEnabled" Type="Bool">true</Property>
		<Property Name="server.vi.propertiesEnabled" Type="Bool">true</Property>
		<Property Name="specify.custom.address" Type="Bool">false</Property>
		<Item Name="sub_VIs" Type="Folder">
			<Item Name="13_EventLogger_callback.vi" Type="VI" URL="../subVIs/13_EventLogger_callback.vi"/>
			<Item Name="15_TimeDifferences_setup.vi" Type="VI" URL="../subVIs/15_TimeDifferences_setup.vi"/>
			<Item Name="createTimeTagger.vi" Type="VI" URL="../subVIs/createTimeTagger.vi"/>
			<Item Name="logger_to_event.vi" Type="VI" URL="../subVIs/logger_to_event.vi"/>
			<Item Name="measureDelayBetweenChannels.vi" Type="VI" URL="../subVIs/measureDelayBetweenChannels.vi"/>
		</Item>
		<Item Name="1_Counter_Time_Trace.vi" Type="VI" URL="../1_Counter_Time_Trace.vi"/>
		<Item Name="2_Cross_Correlation.vi" Type="VI" URL="../2_Cross_Correlation.vi"/>
		<Item Name="3_Cross_Correlation_Part_II.vi" Type="VI" URL="../3_Cross_Correlation_Part_II.vi"/>
		<Item Name="4_Virtual_Channels.vi" Type="VI" URL="../4_Virtual_Channels.vi"/>
		<Item Name="6_Filtering.vi" Type="VI" URL="../6_Filtering.vi"/>
		<Item Name="7_Coincidences-JaggedArrayInLabVIEW.vi" Type="VI" URL="../7_Coincidences-JaggedArrayInLabVIEW.vi"/>
		<Item Name="8_Direct_Time_Tag_Stream_Access.vi" Type="VI" URL="../8_Direct_Time_Tag_Stream_Access.vi"/>
		<Item Name="9_Compensate_Input_Delays_setInputDelay.vi" Type="VI" URL="../9_Compensate_Input_Delays_setInputDelay.vi"/>
		<Item Name="10_Scope.vi" Type="VI" URL="../10_Scope.vi"/>
		<Item Name="11_Histogram2D.vi" Type="VI" URL="../11_Histogram2D.vi"/>
		<Item Name="12_FileWriter_FileReader.vi" Type="VI" URL="../12_FileWriter_FileReader.vi"/>
		<Item Name="13_EventLogger.vi" Type="VI" URL="../13_EventLogger.vi"/>
		<Item Name="14_StartStop_UI.vi" Type="VI" URL="../14_StartStop_UI.vi"/>
		<Item Name="15_HighRes.vi" Type="VI" URL="../15_HighRes.vi"/>
		<Item Name="16_SynchronizedMeasurements.vi" Type="VI" URL="../16_SynchronizedMeasurements.vi"/>
		<Item Name="17_SoftwareClock.vi" Type="VI" URL="../17_SoftwareClock.vi"/>
		<Item Name="18_TimeTaggerNetwork_client.vi" Type="VI" URL="../18_TimeTaggerNetwork_client.vi"/>
		<Item Name="18_TimeTaggerNetwork_server.vi" Type="VI" URL="../18_TimeTaggerNetwork_server.vi"/>
		<Item Name="Dependencies" Type="Dependencies">
			<Item Name="vi.lib" Type="Folder">
				<Item Name="Clear Errors.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Clear Errors.vi"/>
				<Item Name="Generate Temporary File Path.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/libraryn.llb/Generate Temporary File Path.vi"/>
				<Item Name="High Resolution Relative Seconds.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/High Resolution Relative Seconds.vi"/>
				<Item Name="Search and Replace Pattern.vi" Type="VI" URL="/&lt;vilib&gt;/Utility/error.llb/Search and Replace Pattern.vi"/>
				<Item Name="subTimeDelay.vi" Type="VI" URL="/&lt;vilib&gt;/express/express execution control/TimeDelayBlock.llb/subTimeDelay.vi"/>
			</Item>
			<Item Name="fire_logger_event.vi" Type="VI" URL="../subVIs/fire_logger_event.vi"/>
			<Item Name="mscorlib" Type="VI" URL="mscorlib">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
			<Item Name="SwabianInstruments.TimeTagger" Type="Document" URL="SwabianInstruments.TimeTagger">
				<Property Name="NI.PreserveRelativePath" Type="Bool">true</Property>
			</Item>
		</Item>
		<Item Name="Build Specifications" Type="Build"/>
	</Item>
</Project>
