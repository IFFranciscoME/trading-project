
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: A python project for algorithmic trading in FXCM                                           -- #
# -- --------------------------------------------------------------------------------------------------- -- #
# -- script: requirements.txt : text file with the required libraries for the project                    -- #
# -- author: YOUR GITHUB USER NAME                                                                       -- #
# -- license: MIT License                                                                                -- #
# -- --------------------------------------------------------------------------------------------------- -- #
# -- Template repository: https://github.com/IFFranciscoME/trading-project                               -- #
# -- --------------------------------------------------------------------------------------------------- -- #

# -- Packages
import pandas as pd

# -- Other scripts
import data as dt

# -- For massive data download --# 
# data_ohlc = dt.fxcm_ohlc(p_instrument='EUR/USD', p_period='H1',
#                          p_ini='2021-08-01 00:00:00', p_end='2022-01-31 23:59:59')

# -- For offline file data
data_ohlc = pd.read_csv('files/eurusd_6meses.csv', index_col=0)
