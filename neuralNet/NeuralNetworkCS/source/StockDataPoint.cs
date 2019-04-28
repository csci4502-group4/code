namespace NeuralNetworkCS
{
    class StockDataPoint
    {
        public float Open;
        public float High;
        public float Low;
        public float Close;
        public float Volume;

        public StockDataPoint(float open, float high, float low, float close, float volume)
        {
            Open = open;
            High = high;
            Low = low;
            Close = close;
            Volume = volume;
        }
    }
}
