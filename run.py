# 基础库导入

from __future__ import print_function
from __future__ import division

import warnings
warnings.filterwarnings('ignore')
warnings.simplefilter('ignore')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


import os
import sys
# 使用insert 0即只使用github，避免交叉使用了pip安装的abupy，导致的版本不一致问题
sys.path.insert(0, os.path.abspath('../'))
import abupy

# 使用沙盒数据，目的是和书中一样的数据环境
abupy.env.enable_example_env_ipython()

from abupy import abu, EMarketTargetType, AbuMetricsBase, ABuMarketDrawing, ABuProgress, ABuSymbolPd, get_price, ABuIndustries
from abupy import EMarketDataFetchMode, EDataCacheType, EMarketSourceType, FuturesBaseMarket, TCBaseMarket, ABuDateUtil
from abupy import AbuDataParseWrap, StockBaseMarket, SupportMixin, ABuNetWork, Symbol, code_to_symbol

abupy.env.disable_example_env_ipython()

abupy.env.g_market_source = EMarketSourceType.E_MARKET_SOURCE_tx
abupy.env.g_data_cache_type = EDataCacheType.E_DATA_CACHE_CSV
abu.run_kl_update(start='2023-06-01', end='2023-07-02', market=EMarketTargetType.E_MARKET_TARGET_CN, n_jobs=10)
