import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import Stack from '@mui/material/Stack';
import Grid from '@mui/material/Unstable_Grid2';
import axios from 'axios';
import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useApp } from 'src/context/app-context';

import './app-styles.css';
import SearchBar from './SearchBar';
import ProductFilters from 'src/sections/products/product-filters';
import ProductSort from 'src/sections/products/product-sort';
import ProductCard from 'src/sections/products/product-card';

export default function AppView() {
  const { data, setData, dataArr, setDataArr } = useApp();
  const [searchValue, setSearchValue] = useState('');
  const navigate = useNavigate();
  const handleSearchChange = (event) => {
    setSearchValue(event.target.value);
  };
  const [searchLoad, setSearchLoad] = useState(false);
  const [openFilter, setOpenFilter] = useState(false);
  const handleOpenFilter = () => {
    setOpenFilter(true);
    console.log(data);
  };
  const handleCloseFilter = () => {
    setOpenFilter(false);
  };

  const getScrapedData = async () => {
    await axios
      .get(`http://127.0.0.1:8000/product/?title=${searchValue}`)
      .then((response) => {
        console.log(response?.data);
        if (response?.data) {
          const arr = [
            ...response.data.flipkart,
            ...response.data.ebay,
            ...response.data.indiamart,
          ];
          setDataArr(arr);
          getCombinedStats(response?.data, arr);
          setSearchLoad(true);
        }
      })
      .catch((error) => console.log(error));
  };

  const numberWithoutCommas = (num) => Number(num.replace(/,/g, ''));

  const getCombinedStats = (obj, arr) => {
    let flipkartReview = 0;
    let ebayReview = 0;
    let indiamartReview = 0;
    let flipkartPrice = 0;
    let ebayPrice = 0;
    let indiamartPrice = 0;

    arr.forEach((item) => {
      if (item?.source?.toLowerCase() === 'flipkart') {
        flipkartReview += numberWithoutCommas(item.reviews_count);
        // flipkartPrice += Number(item.price);
      } else if (item?.source?.toLowerCase() === 'ebay') {
        ebayReview += numberWithoutCommas(item.reviews_count);
        // ebayPrice += Number(item.price);
      } else {
        indiamartReview += numberWithoutCommas(item.reviews_count);
        // indiamartPrice += Number(item.price);
      }
    });

    setData({
      ...obj,
      // flipkartPrice,
      flipkartReview,
      // ebayPrice,
      ebayReview,
      // indiamartPrice,
      indiamartReview,
    });
  };

  return (
    <>
      {!searchLoad ? (
        <Container maxWidth="4xl" className="app-container">
          {/* <Typography variant="h4" sx={{ mb: 5, textAlign: 'center' }}>
            eCompare
          </Typography> */}
          <h1 style={{ fontSize: '4rem', fontWeight: 'bold', color: '#333', textAlign: 'center' }}>
            Ecompare
          </h1>
          <Typography
            variant="body1"
            className="desc1 text"
            style={{
              fontSize: '1.6rem',
              whiteSpace: 'nowrap',
              textAlign: 'center',
              justifyContent: 'center',
            }}
          >
            A platform for comparing prices of various products across different online stores.
          </Typography>
          <Typography
            variant="h3"
            className="desc1 text"
            style={{
              fontSize: '1.8rem',
              textAlign: 'center',
              justifyContent: 'center',
              fontWeight: 'bold',
              backgroundImage: 'linear-gradient(to right, #0072ff, #00c6ff)',
              WebkitBackgroundClip: 'text',
              color: 'transparent',
            }}
          >
            Best Deals-Recommendations-Analysis
          </Typography>
          <Typography variant="body1" className="desc2">
            Try searching <span className="animated" />
          </Typography>
          <div className="search-container">
            <SearchBar
              label="Search products..."
              variant="outlined"
              value={searchValue}
              onChange={handleSearchChange}
            />
            <button type="submit" className="search-button" onClick={getScrapedData}>
              Compare
            </button>
          </div>
        </Container>
      ) : (
        <Container>
          <Typography variant="h3" sx={{ mb: 3 }}>
            Search Results for {searchValue}
          </Typography>
          <Typography variant="h4" sx={{ mb: 2 }}>
            {dataArr?.length} most relevant results...
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
            {dataArr.map((product, index) => (
              <Grid key={index} xs={12} sm={6} md={3}>
                <ProductCard product={product} />
              </Grid>
            ))}
          </Grid>
        </Container>
      )}
    </>
  );
}
