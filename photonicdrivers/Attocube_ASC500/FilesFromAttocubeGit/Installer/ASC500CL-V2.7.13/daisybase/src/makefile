#*******************************************************************************
#  Project:        ASC500 Custom Library
#
#  Filename:       makefile
#
#  Purpose:        MSVC makefile for example
#
#  Author:         N-Hands GmbH & Co KG
#*******************************************************************************
# $Id: makefile.win,v 1.4 2016/12/01 18:02:32 trurl Exp $

example500.exe : example500.obj ..\lib\daisybase.lib
	link /NOLOGO /DEBUG /SUBSYSTEM:CONSOLE example500.obj ..\lib\daisybase.lib

example500.obj :  example500.c
	cl -nologo -c -W3 -Zi -MDd -I..\include example500.c 

