import { useEffect, useState } from 'react';

import Stack from '@mui/material/Stack';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Unstable_Grid2';
import Typography from '@mui/material/Typography';

import { products } from 'src/_mock/products';

import ProductCard from '../product-card';
import ProductSort from '../product-sort';
import ProductFilters from '../product-filters';
import { useApp } from 'src/context/app-context';

export default function ProductsView() {
  const [openFilter, setOpenFilter] = useState(false);
  const { data, setData, dataBlog, setDataBlog } = useApp();
  const handleOpenFilter = () => {
    setOpenFilter(true);
    console.log(data);
    console.log(dataBlog);
  };

  useEffect(() => {
    return () => {
      let temp = [];
      if (data?.flipkart?.length >= 2) {
        temp.push(data.flipkart[0]);
        temp.push(data.flipkart[1]);
      } else {
        temp = [...temp, ...data.flipkart];
      }
      if (data?.ebay?.length >= 2) {
        temp.push(data.ebay[0]);
        temp.push(data.ebay[1]);
      } else {
        temp = [...temp, ...data.ebay];
      }
      if (data?.indiamart?.length >= 2) {
        temp.push(data.indiamart[0]);
        temp.push(data.indiamart[1]);
      } else {
        temp = [...temp, ...data.indiamart];
      }
      setDataBlog(temp);
      console.log(temp);
    };
  }, [data]);

  const handleCloseFilter = () => {
    setOpenFilter(false);
  };

  return (
    <Container>
      <Typography variant="h4" sx={{ mb: 5 }}>
        Search Results
      </Typography>

      <Stack
        direction="row"
        alignItems="center"
        flexWrap="wrap-reverse"
        justifyContent="flex-end"
        sx={{ mb: 5 }}
      >
        <Stack direction="row" spacing={1} flexShrink={0} sx={{ my: 1 }}>
          <ProductFilters
            openFilter={openFilter}
            onOpenFilter={handleOpenFilter}
            onCloseFilter={handleCloseFilter}
          />

          <ProductSort />
        </Stack>
      </Stack>

      <Grid container spacing={3}>
        {/* {products.map((product) => (
          <Grid key={product.id} xs={12} sm={6} md={3}>
            <ProductCard product={product} />
          </Grid>
        ))} */}
        {dataBlog.map((product, index) => (
          <Grid key={index} xs={12} sm={6} md={3}>
            <ProductCard product={product} />
          </Grid>
        ))}
      </Grid>
    </Container>
  );
}
