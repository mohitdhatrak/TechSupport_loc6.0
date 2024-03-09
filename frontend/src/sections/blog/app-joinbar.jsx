import PropTypes from 'prop-types';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import { fNumber } from 'src/utils/format-number';
import Chart, { useChart } from 'src/components/chart';

// ----------------------------------------------------------------------

export default function AppJoinbar({ title, subheader, chart, ...other }) {
  const { colors, series, options } = chart;

  const chartData = series.reduce((acc, curr) => {
    if (Array.isArray(curr.data)) {
      return [...acc, ...curr.data];
    } else {
      console.error('Data is not iterable:', curr.data);
      return acc;
    }
  }, []);

  const chartOptions = useChart({
    colors,
    tooltip: {
      marker: { show: false },
      y: {
        formatter: (value) => fNumber(value),
        title: {
          formatter: () => '',
        },
      },
    },
    plotOptions: {
      bar: {
        horizontal: true,
        barHeight: '28%',
        borderRadius: 2,
      },
    },
    xaxis: {
      categories: series.map((s) => s.label).flat(), // Flatten the array of labels
    },
    ...options,
  });

  return (
    <Card {...other}>
      <CardHeader title={title} subheader={subheader} />
      <Box sx={{ mx: 3 }}>
        <Chart
          dir="ltr"
          type="bar"
          series={[{ data: chartData }]} // Use the concatenated data array
          options={chartOptions}
          width="100%"
          height={364}
        />
      </Box>
    </Card>
  );
}

AppJoinbar.propTypes = {
  chart: PropTypes.object,
  subheader: PropTypes.string,
  title: PropTypes.string,
};
