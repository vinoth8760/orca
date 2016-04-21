#!/usr/bin/python

from macaroon.playback import *
import utils

sequence = MacroSequence()

sequence.append(PauseAction(5000))
sequence.append(KeyComboAction("Tab"))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyPressAction(0, None, "KP_Insert"))
sequence.append(KeyComboAction("KP_Enter"))
sequence.append(KeyReleaseAction(0, None, "KP_Insert"))
sequence.append(utils.AssertPresentationAction(
    "1. Title bar",
    ["BRAILLE LINE:  'Links to test files - Nightly'",
     "     VISIBLE:  'Links to test files - Nightly', cursor=0",
     "SPEECH OUTPUT: 'Links to test files - Nightly'"]))

sequence.append(PauseAction(5000))

sequence.append(utils.StartRecordingAction())
sequence.append(KeyPressAction(0, None, "KP_Insert"))
sequence.append(KeyComboAction("KP_Enter"))
sequence.append(KeyComboAction("KP_Enter"))
sequence.append(KeyReleaseAction(0, None, "KP_Insert"))
sequence.append(utils.AssertPresentationAction(
    "2. Status bar",
    ["BRAILLE LINE:  'Links to test files - Nightly'",
     "     VISIBLE:  'Links to test files - Nightly', cursor=0",
     "BRAILLE LINE:  'anchors.html'",
     "     VISIBLE:  'anchors.html', cursor=1",
     "BRAILLE LINE:  'anchors.html'",
     "     VISIBLE:  'anchors.html', cursor=1",
     "BRAILLE LINE:  'file:///.+/anchors.html'",
     "     VISIBLE:  'file:///.+', cursor=0",
     "SPEECH OUTPUT: 'Links to test files - Nightly'",
     "SPEECH OUTPUT: 'file:///.+/anchors.html'"]))

sequence.append(utils.AssertionSummaryAction())
sequence.start()
