#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Top Block
# Generated: Fri Jan 24 18:49:31 2020
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

from PyQt5 import Qt, QtCore
from gnuradio import audio
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import filter
from gnuradio import gr
from gnuradio import vocoder
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import sys
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
        self.ssCVSD = ssCVSD = 2
        self.payload = payload = 128
        self.nbConst = nbConst = 64
        self.bwCVSD = bwCVSD = 0.3

        ##################################################
        # Blocks
        ##################################################
        self.vocoder_cvsd_encode_fb_0 = vocoder.cvsd_encode_fb(ssCVSD,bwCVSD)
        self.vocoder_cvsd_decode_bf_0 = vocoder.cvsd_decode_bf(ssCVSD,bwCVSD)
        self.rational_resampler_xxx_0 = filter.rational_resampler_fff(
                interpolation=1,
                decimation=1,
                taps=None,
                fractional_bw=None,
        )
        self.digital_ofdm_tx_0 = digital.ofdm_tx(
        	  fft_len=64, cp_len=16,
        	  packet_length_tag_key="packet_len",
        	  bps_header=1,
        	  bps_payload=1,
        	  rolloff=0,
        	  debug_log=False,
        	  scramble_bits=False
        	 )
        self.digital_ofdm_rx_0 = digital.ofdm_rx(
        	  fft_len=64, cp_len=16,
        	  frame_length_tag_key='frame_'+"packet_len",
        	  packet_length_tag_key="packet_len",
        	  bps_header=1,
        	  bps_payload=1,
        	  debug_log=False,
        	  scramble_bits=False
        	 )
        self.blocks_wavfile_source_1 = blocks.wavfile_source('/home/tarnagda/Documents/Transmission/WAVs/streetwave.wav', True)
        self.blocks_tag_gate_0 = blocks.tag_gate(gr.sizeof_gr_complex * 1, False)
        self.blocks_stream_to_tagged_stream_0 = blocks.stream_to_tagged_stream(gr.sizeof_char, 1, payload, "packet_len")
        self.audio_sink_0 = audio.sink(44100, '', True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_stream_to_tagged_stream_0, 0), (self.digital_ofdm_tx_0, 0))
        self.connect((self.blocks_tag_gate_0, 0), (self.digital_ofdm_rx_0, 0))
        self.connect((self.blocks_wavfile_source_1, 0), (self.vocoder_cvsd_encode_fb_0, 0))
        self.connect((self.digital_ofdm_rx_0, 0), (self.vocoder_cvsd_decode_bf_0, 0))
        self.connect((self.digital_ofdm_tx_0, 0), (self.blocks_tag_gate_0, 0))
        self.connect((self.rational_resampler_xxx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.vocoder_cvsd_decode_bf_0, 0), (self.rational_resampler_xxx_0, 0))
        self.connect((self.vocoder_cvsd_encode_fb_0, 0), (self.blocks_stream_to_tagged_stream_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "top_block")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_ssCVSD(self):
        return self.ssCVSD

    def set_ssCVSD(self, ssCVSD):
        self.ssCVSD = ssCVSD

    def get_payload(self):
        return self.payload

    def set_payload(self, payload):
        self.payload = payload
        self.blocks_stream_to_tagged_stream_0.set_packet_len(self.payload)
        self.blocks_stream_to_tagged_stream_0.set_packet_len_pmt(self.payload)

    def get_nbConst(self):
        return self.nbConst

    def set_nbConst(self, nbConst):
        self.nbConst = nbConst

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
