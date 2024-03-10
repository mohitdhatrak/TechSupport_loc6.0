import Stack from '@mui/material/Stack';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';

import { useApp } from 'src/context/app-context';

import ProdComp from './prodComp';
import AppCurrentVisits from '../app-current-visits';
import AppConversionRates from '../app-conversion-rates';

export default function BlogView() {
  const { data } = useApp();
  console.log(data);

  const title =
    data?.flipkart?.length > 0
      ? data?.flipkart[0]?.title
      : data?.ebay?.length > 0
      ? data?.ebay[0]?.title
      : data?.indiamart[0]?.title;

  return (
    <Container>
      <Stack direction="row" alignItems="center" justifyContent="space-between" mb={0}>
        <Typography variant="h4">{title}</Typography>
      </Stack>

      <ProdComp />

      <Stack direction="row" alignItems="center" justifyContent="space-between" mb={2}>
        <Typography variant="h4">Comparison and Analysis</Typography>
      </Stack>

      <div style={{ display: 'flex', flexDirection: 'row', gap: '20px', marginBottom: '3rem' }}>
        <AppCurrentVisits
          title="Reviews count"
          chart={{
            series: [
              { label: 'Flipkart', value: data?.flipkartReview },
              { label: 'eBay', value: data?.ebayReview },
              { label: 'IndiaMart', value: data?.indiamartReview },
            ],
          }}
        />

        <AppConversionRates
          title="Price comparison"
          chart={{
            series: [
              { label: 'Flipkart', value: data?.flipkartPrice },
              { label: 'eBay', value: data?.ebayPrice },
              { label: 'IndiaMart', value: data?.indiamartPrice },
            ],
          }}
        />
      </div>
    </Container>
  );
}
