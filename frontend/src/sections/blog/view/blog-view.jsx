import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Unstable_Grid2';
import Typography from '@mui/material/Typography';

import { posts } from 'src/_mock/blog';

import Iconify from 'src/components/iconify';

import PostCard from '../post-card';
import PostSort from '../post-sort';
import PostSearch from '../post-search';
import ProdComp from './prodComp';
import AppCurrentVisits from '../app-current-visits';
import AppConversionRates from '../app-conversion-rates';
import AppJoinbar from '../app-joinbar';

export default function BlogView() {
  return (
    <Container>
      <Stack direction="row" alignItems="center" justifyContent="space-between" mb={5}>
        <Typography variant="h4">Blog</Typography>

        <Button variant="contained" color="inherit" startIcon={<Iconify icon="eva:plus-fill" />}>
          New Post
        </Button>
      </Stack>

      <Stack mb={5} direction="row" alignItems="center" justifyContent="space-between">
        <PostSearch posts={posts} />
        <PostSort
          options={[
            { value: 'latest', label: 'Latest' },
            { value: 'popular', label: 'Popular' },
            { value: 'oldest', label: 'Oldest' },
          ]}
        />
      </Stack>

      {/* <Grid container spacing={3}>
        {posts.map((post, index) => (
          <PostCard key={post.id} post={post} index={index} />
        ))}
      </Grid> */}
      <ProdComp />
      <div style={{ display: 'flex', flexDirection: 'row', gap: '20px' }}>
        {/* <Grid xs={12} sm={6} md={4} lg={3}> */}
        <AppCurrentVisits
          title="Price pie"
          chart={{
            series: [
              { label: 'Amazon', value: 4344 },
              { label: 'Flipkart', value: 5435 },
              { label: 'Myntra', value: 1443 },
              { label: 'Ebay', value: 4443 },
            ],
          }}
        />
        {/* </Grid> */}
        {/* <Grid xs={12} md={6} lg={8}> */}
        <AppConversionRates
          title="Conversion Rates"
          subheader="(+43%) than last year"
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
        {/* </Grid> */}
        {/* <AppJoinbar
          title="Conversion Rates"
          subheader="(+43%) than last year"
          chart={{
            series: [
              { label: 'Italy', value: [400, 300] },
              { label: 'Japan', value: [430, 300] },
              { label: 'China', value: [448, 300] },
              { label: 'Canada', value: [470, 300] },
              { label: 'France', value: [540, 300] },
              { label: 'Germany', value: [580, 300] },
              { label: 'South Korea', value: [690, 300] },
              { label: 'Netherlands', value: [1100, 300] },
              { label: 'United States', value: [1200, 300] },
              { label: 'United Kingdom', value: [1380, 300] },
            ],
          }}
        /> */}
      </div>
    </Container>
  );
}
