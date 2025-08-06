How to use the Time Tagger C++ library on Windows.

Compiler Requirements
* Microsoft Visual C++ (MSVC), Intel C++ Compiler (ICC) or Clang

Note: MinGW is not binary compatible and, therefore, cannot be used.

We provide the import library (.lib) and the shared library (.dll) for two C++ ABIs.
Please link your application statically to the import library.
* TimeTagger.lib / TimeTagger.dll for MultiThreadedDLL /MD (Microsoft Runtime Library)
* TimeTaggerD.lib / TimeTaggerD.dll for MultiThreadedDebugDLL /MDd (Microsoft Runtime Library)

Both libraries require that the final application is linked to at least version v143 of the Visual Studio platform toolset (default in Visual Studio 2022).

The following include path must be added:
* $(TIMETAGGER_INSTALL_PATH)\driver\include

and the for 64 bit the following library path:
* $(TIMETAGGER_INSTALL_PATH)\driver\include\x64

An example project for Microsoft Visual Studio can be found in the folder of the Readme:
* Quickstart.vcxproj
