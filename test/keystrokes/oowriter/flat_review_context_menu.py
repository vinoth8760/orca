#!/usr/bin/python

from macaroon.playback import *
import utils

sequence = MacroSequence()

sequence.append(PauseAction(3000))
sequence.append(KeyComboAction("<Shift>F10"))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("KP_8"))
sequence.append(utils.AssertPresentationAction(
    "1. Review current line",
    ["BRAILLE LINE:  'Paste $l'",
     "     VISIBLE:  'Paste $l', cursor=1",
     "SPEECH OUTPUT: 'Paste'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("KP_7"))
sequence.append(utils.AssertPresentationAction(
    "2. Review previous line",
    [""]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("KP_9"))
sequence.append(utils.AssertPresentationAction(
    "3. Review next line",
    ["BRAILLE LINE:  'separator $l'",
     "     VISIBLE:  'separator $l', cursor=1",
     "SPEECH OUTPUT: 'separator'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("KP_9"))
sequence.append(utils.AssertPresentationAction(
    "4. Review next line",
    ["BRAILLE LINE:  'Paste Special $l'",
     "     VISIBLE:  'Paste Special $l', cursor=1",
     "SPEECH OUTPUT: 'Paste Special'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("KP_9"))
sequence.append(utils.AssertPresentationAction(
    "5. Review next line",
    ["BRAILLE LINE:  'separator $l'",
     "     VISIBLE:  'separator $l', cursor=1",
     "SPEECH OUTPUT: 'separator'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("KP_9"))
sequence.append(utils.AssertPresentationAction(
    "6. Review next line",
    ["BRAILLE LINE:  'Clear Direct Formatting $l'",
     "     VISIBLE:  'Clear Direct Formatting $l', cursor=1",
     "SPEECH OUTPUT: 'Clear Direct Formatting'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("KP_9"))
sequence.append(utils.AssertPresentationAction(
    "7. Review next line",
    ["BRAILLE LINE:  'separator $l'",
     "     VISIBLE:  'separator $l', cursor=1",
     "SPEECH OUTPUT: 'separator'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("KP_9"))
sequence.append(utils.AssertPresentationAction(
    "8. Review next line",
    ["BRAILLE LINE:  'Character... $l'",
     "     VISIBLE:  'Character... $l', cursor=1",
     "SPEECH OUTPUT: 'Character...'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("KP_9"))
sequence.append(utils.AssertPresentationAction(
    "9. Review next line",
    ["BRAILLE LINE:  'Paragraph... $l'",
     "     VISIBLE:  'Paragraph... $l', cursor=1",
     "SPEECH OUTPUT: 'Paragraph...'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("KP_9"))
sequence.append(utils.AssertPresentationAction(
    "10. Review next line",
    ["BRAILLE LINE:  'Bullets and Numbering... $l'",
     "     VISIBLE:  'Bullets and Numbering... $l', cursor=1",
     "SPEECH OUTPUT: 'Bullets and Numbering...'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("KP_9"))
sequence.append(utils.AssertPresentationAction(
    "11. Review next line",
    ["BRAILLE LINE:  'Page... $l'",
     "     VISIBLE:  'Page... $l', cursor=1",
     "SPEECH OUTPUT: 'Page...'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("KP_9"))
sequence.append(utils.AssertPresentationAction(
    "12. Review next line",
    ["BRAILLE LINE:  'Change Case $l'",
     "     VISIBLE:  'Change Case $l', cursor=1",
     "SPEECH OUTPUT: 'Change Case'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("KP_9"))
sequence.append(utils.AssertPresentationAction(
    "13. Review next line",
    ["BRAILLE LINE:  'separator $l'",
     "     VISIBLE:  'separator $l', cursor=1",
     "SPEECH OUTPUT: 'separator'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("KP_9"))
sequence.append(utils.AssertPresentationAction(
    "14. Review next line",
    ["BRAILLE LINE:  'Edit Paragraph Style... $l'",
     "     VISIBLE:  'Edit Paragraph Style... $l', cursor=1",
     "SPEECH OUTPUT: 'Edit Paragraph Style...'"]))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyComboAction("KP_9"))
sequence.append(utils.AssertPresentationAction(
    "15. Review next line",
    [""]))

sequence.append(utils.AssertionSummaryAction())
sequence.start()

