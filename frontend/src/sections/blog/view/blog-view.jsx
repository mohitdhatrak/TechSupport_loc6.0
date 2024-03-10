import Stack from '@mui/material/Stack';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';

import { useApp } from 'src/context/app-context';

import ProdComp from './prodComp';
import AppCurrentVisits from '../app-current-visits';
import AppConversionRates from '../app-conversion-rates';

export default function BlogView() {
  const { data } = useApp();

  return (
    <Container>
      <Stack direction="row" alignItems="center" justifyContent="space-between" mb={2}>
        <Typography variant="h4">Comparison and Analysis</Typography>
      </Stack>

      <ProdComp />

      <div style={{ display: 'flex', flexDirection: 'row', gap: '20px' }}>
        <AppCurrentVisits
          title="Reviews count"
          chart={{
            series: [
              { label: 'Flipkart', value: Number(data?.flipkartReview) },
              { label: 'eBay', value: Number(data?.ebayReview) },
              { label: 'IndiaMart', value: Number(data?.indiamartReview) },
            ],
          }}
        />

        <AppConversionRates
          title="Ratings"
          chart={{
            series: [
              { label: 'Italy', value: 400 },
              { label: 'Japan', value: 430 },
              { label: 'China', value: 448 },
              { label: 'Canada', value: 470 },
              { label: 'France', value: 540 },
              { label: 'Germany', value: 580 },
              { label: 'South Korea', value: 690 },
              { label: 'Netherlands', value: 1100 },
              { label: 'United States', value: 1200 },
              { label: 'United Kingdom', value: 1380 },
            ],
          }}
        />
      </div>
    </Container>
  );
}
