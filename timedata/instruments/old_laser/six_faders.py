from . import constants, abs_lfo_fader


class SixFaders:
    def __init__(self, **kwds):
        super().__init__(kwds)
        self.faders = []
        channels = list(constants.Channels)[2:]
        for i, channel in enumerate(channels):
            fader = abs_lfo_fader.AbsLfoFader(
                self, channel.pretty_string(), print)
            # fader.pack(side=tk.LEFT)
            self.faders.append(fader)
