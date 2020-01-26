#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Wed Jan 22 18:03:27 2020
##################################################

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt5 import Qt
from PyQt5 import Qt, QtCore
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio import vocoder
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sip
import sys
import time
from gnuradio import qtgui


class top_block(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Top Block")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "top_block")

        if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
            self.restoreGeometry(self.settings.value("geometry").toByteArray())
        else:
            self.restoreGeometry(self.settings.value("geometry", type=QtCore.QByteArray))

        ##################################################
        # Variables
        ##################################################
        self.ssQAM = ssQAM = 2
        self.ssCVSD = ssCVSD = 8
        self.samp_rate = samp_rate = 1500000
        self.resamp = resamp = 8
        self.nbConst = nbConst = 4
        self.freq_port = freq_port = 867000000
        self.decim = decim = 8
        self.cutoffFreq = cutoffFreq = 44100*8
        self.bwQAM = bwQAM = 0.7
        self.bwCVSD = bwCVSD = 0.7

        ##################################################
        # Blocks
        ##################################################
        self.vocoder_cvsd_encode_fb_0 = vocoder.cvsd_encode_fb(ssCVSD,bwCVSD)
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join(("", "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(freq_port, 0)
        self.uhd_usrp_sink_0.set_gain(70, 0)
        self.uhd_usrp_sink_0.set_antenna('TX/RX', 0)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
        	2048, #size
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_x_axis(-2, 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)

        if not True:
          self.qtgui_const_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "red", "red", "red",
                  "red", "red", "red", "red", "red"]
        styles = [0, 0, 0, 0, 0,
                  0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
                   0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.digital_qam_mod_0 = digital.qam.qam_mod(
          constellation_points=nbConst,
          mod_code="gray",
          differential=False,
          samples_per_symbol=ssQAM,
          excess_bw=bwQAM,
          verbose=False,
          log=False,
          )
        self.blocks_wavfile_source_1 = blocks.wavfile_source('/home/tarnagda/Documents/Transmission/WAVs/banana.wav', True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_wavfile_source_1, 0), (self.vocoder_cvsd_encode_fb_0, 0))
        self.connect((self.digital_qam_mod_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.digital_qam_mod_0, 0), (self.uhd_usrp_sink_0, 0))
        self.connect((self.vocoder_cvsd_encode_fb_0, 0), (self.digital_qam_mod_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_ssQAM(self):
        return self.ssQAM

    def set_ssQAM(self, ssQAM):
        self.ssQAM = ssQAM

    def get_ssCVSD(self):
        return self.ssCVSD

    def set_ssCVSD(self, ssCVSD):
        self.ssCVSD = ssCVSD

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)

    def get_resamp(self):
        return self.resamp

    def set_resamp(self, resamp):
        self.resamp = resamp

    def get_nbConst(self):
        return self.nbConst

    def set_nbConst(self, nbConst):
        self.nbConst = nbConst

    def get_freq_port(self):
        return self.freq_port

    def set_freq_port(self, freq_port):
        self.freq_port = freq_port
        self.uhd_usrp_sink_0.set_center_freq(self.freq_port, 0)

    def get_decim(self):
        return self.decim

    def set_decim(self, decim):
        self.decim = decim

    def get_cutoffFreq(self):
        return self.cutoffFreq

    def set_cutoffFreq(self, cutoffFreq):
        self.cutoffFreq = cutoffFreq

    def get_bwQAM(self):
        return self.bwQAM

    def set_bwQAM(self, bwQAM):
        self.bwQAM = bwQAM

    def get_bwCVSD(self):
        return self.bwCVSD

    def set_bwCVSD(self, bwCVSD):
        self.bwCVSD = bwCVSD


def main(top_block_cls=top_block, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
