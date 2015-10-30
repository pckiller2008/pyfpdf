# Testing #

This page describe test suite within PyFPDF library.

This page applicable to version 1.7.1 and newer (from trunk).

## Old tests ##

There are old test from stone-age. It will be remove when test suite completely overfill all old tests.

## Purposes ##

  * Cover all fixed issues
  * Reach **byte-to-byte accuracy** with all python versions (2.x and 3.x)
  * Alarm when required changes in library breaks something

## Quick start ##

Installed copy:
  * Goto to tests folder
  * Run `python runtest.py`

Local copy:
  * Goto to tests folder
  * set PYFPDFTESTLOCAL variable
  * Run `prepare_local`
  * Run `python runtest.py`

You can specify tests and/or interpretors list with `--test` and `--interp` arguments. For detailed information see `--help`.

Please note, batch operations test required minimum in library, but when you call one test directly with `python cover/text_xx.py` PDF output (if any) may differ.

## Structure ##

  * cover - all new tests
  * fpdf\_local - local copy fpdf, generated by prepare\_local
  * out-x.x.x - working directory for python x.x.x
  * runtest.py - batch tester
  * resources.txt - resources list
  * data files
  * old tests etc.

Every test can be executed as standalone app as from `tests/cover` or from `tests/out-x.x.x` folder. You can use `--downloadfonts` argument for `runtest.py`.

## Fonts ##

Some (most) tests uses font pack http://pyfpdf.googlecode.com/files/fpdf_unicode_font_pack.zip

Place .ttf files in tests/font folder.

## Test template ##

File `tests/cover/test_template.py` contains all additional information.

Variables:
  * format - PDF, TXT
  * fn - result filename (if test did't produce any external file it can be omitted)
  * hash - hash when in file created in automatic test mode
  * 2to3 - use 2to3 tool (default - no)
  * python2 - this test can be used with python2 (default - yes)
  * python3 - this test can be used with python3 (default - yes)
  * pil - PIL or Pillow module is required (default - no)
  * platform - platform for this test (win32, linux2, etc, by default all - 