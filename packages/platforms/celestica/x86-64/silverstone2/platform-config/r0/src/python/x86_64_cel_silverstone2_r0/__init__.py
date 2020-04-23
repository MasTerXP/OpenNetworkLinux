from onl.platform.base import *
from onl.platform.celestica import *

class OnlPlatform_x86_64_cel_silverstone2_r0(OnlPlatformCelestica,
                                            OnlPlatformPortConfig_48x10_6x40):
    PLATFORM='x86-64-cel-silverstone2-r0'
    MODEL="Silverstone2"
    SYS_OBJECT_ID=".2060.1"
