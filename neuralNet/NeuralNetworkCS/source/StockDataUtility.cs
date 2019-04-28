using System.Collections.Generic;
using Microsoft.VisualBasic.FileIO;

namespace NeuralNetworkCS
{
    static class StockDataUtility
    {
        public static List<StockDataPoint> ReadStockFile(string path)
        {
            List<StockDataPoint> dataPoints = new List<StockDataPoint>();
            TextFieldParser csvParser = new TextFieldParser(path);
            csvParser.TextFieldType = FieldType.Delimited;
            csvParser.SetDelimiters(",");
            csvParser.ReadFields(); // Skip first line.
            while (!csvParser.EndOfData)
            {
                string[] p = csvParser.ReadFields();
                float open = float.Parse(p[1]);
                float high = float.Parse(p[2]);
                float low = float.Parse(p[3]);
                float close = float.Parse(p[4]);
                float volume = float.Parse(p[5]);
                StockDataPoint dataPoint = new StockDataPoint(open, high, low, close, volume);
                dataPoints.Add(dataPoint);

            }
            csvParser.Close();
            return dataPoints;
        }

        public static float NormalizeValue(float low, float high, float actual)
        {
            float num = actual - low;
            float den = high - low;
            return num / den;
        }
    }
}
