######MA######
'''
//@version=4
study("yaxuan_test1",shorttitle='sma',overlay=true)
sma_period=input(defval=30,title='sma_period',minval=10,type=input.integer)

dev_percent = input(defval=0.03,title='dev_percent,minval=0.001,type=input.float')

sma_value = sma(close,sma_period)
sma_up = sma_value*(1+dev_percent)
sma_down = sma_value*(1-dev_percent)

plot(sma_value,linewidth=3,color=color.green)
plot(sma_up,linewidth=1,color=color.red)
plot(sma_down,linewidth=1,color=color.red)

#可以跌破下均线则做空，突破上均线则做多
#也可以用中均线添加平仓方式
'''

'''
//@version=4
study("yaxuan_test2", shorttitle="sma", overlay=true)

// short_period= input(defval=30, title="sma_period", minval=10, type=input.integer)
long_period= input(defval=30, title="sma_period", minval=20, type=input.integer)

sma_long_period = input(defval=10, title="sma_long_period", minval=5, type=input.integer)

// short_sma_value = sma(close, short_period)
long_sma_vlaue = sma(close, long_period)
sma_long_sma_value = sma(long_sma_vlaue, sma_long_period)


plot(long_sma_vlaue, color=color.red, linewidth=3)
plot(sma_long_sma_value, color=color.green, linewidth=3)

#双均线金叉&死叉，在bitcoin感觉不适用

'''
