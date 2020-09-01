# Andre-SMA-Alpaca-TradingView-place-order

Use below for TradingView alert.  Web hook can be generated from AWS Chalice

more information can be found here
https://www.youtube.com/playlist?list=PLvzuUVysUFOsdO_i_VSsKpao-2vpLijzk

{
    "open": {{open}},
    "high": {{high}},
    "low": {{low}},
    "close": {{close}},
    "exchange": "{{exchange}}",
    "ticker": "{{ticker}}",
    "volume": {{volume}},
    "time": "{{time}}",
    "timenow": "{{timenow}}",
    "side": "{{strategy.order.action}}"
}
