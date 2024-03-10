import Stack from '@mui/material/Stack';
import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';

import { useApp } from 'src/context/app-context';

import ProdComp from './prodComp';
import AppCurrentVisits from '../app-current-visits';
import AppConversionRates from '../app-conversion-rates';
import { useEffect, useState } from 'react';
import axios from 'axios';
import AppWebsiteVisits from '../app-website-visits';

export default function BlogView() {
  const { data } = useApp();
  const [sentiment, setSentiment] = useState({ ebay: 3, flipkart: 5, indiamart: 3.5 });
  console.log(data);

  useEffect(() => {
    axios
      .post('http://127.0.0.1:8000/average_sentiment', data, {
        headers: {
          'Content-Type': 'application/json',
        },
      })
      .then((response) => {
        console.log(response?.data);
        setSentiment(response?.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

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

      <div style={{ marginTop: '20px', marginBottom: '20px' }}>
        <AppWebsiteVisits
          title="Price Tracking"
          subheader="Find about all all the sales"
          chart={{
            labels: [
              '01/01/2003',
              '02/01/2003',
              '03/01/2003',
              '04/01/2003',
              '05/01/2003',
              '06/01/2003',
              '07/01/2003',
              '08/01/2003',
              '09/01/2003',
              '10/01/2003',
              '11/01/2003',
            ],
            series: [
              {
                name: 'Amazon',
                type: 'area',
                fill: 'gradient',
                data: [23, 11, 22, 27, 13, 22, 37, 21, 44, 22, 30],
              },
              {
                name: 'Flipkart',
                type: 'area',
                fill: 'gradient',
                data: [44, 55, 41, 67, 22, 43, 21, 41, 56, 27, 43],
              },
              {
                name: 'Ebay',
                type: 'area',
                fill: 'gradient',
                data: [30, 25, 36, 30, 45, 35, 64, 52, 59, 36, 39],
              },
            ],
          }}
        />
      </div>

      <Stack direction="row" alignItems="center" justifyContent="space-between" mb={2}>
        <Typography variant="h4">Sentiment Analysis Score</Typography>
      </Stack>
      <div className="container">
        {Object.entries(sentiment).map(([company, score], index) => (
          <div className="item" key={index}>
            <span className="company-name">{company}</span>
            <span className="sentiment-score">{score}</span>
          </div>
        ))}
      </div>
    </Container>
  );
}
