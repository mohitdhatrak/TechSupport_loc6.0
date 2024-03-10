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

  const numberWithoutCommas = (str) => Number(str.replace(/,/g, '').trim());
  const removeCurrencySymbols = (str) => Number(str.replace(/[₹$a-zA-Z, ]/g, '').trim());

  const getCombinedStats = (obj, arr) => {
    let flipkartReview = 0;
    let ebayReview = 0;
    let indiamartReview = 0;
    let flipkartPrice = 0;
    let ebayPrice = 0;
    let indiamartPrice = 0;
    let flipkart = 0;
    let ebay = 0;
    let indiamart = 0;

    // arr.forEach((item) => {
    //   const reviews = numberWithoutCommas(
    //     typeof item.reviews_count === 'string' ? item.reviews_count : toString(item.reviews_count)
    //   );
    //   const price = removeCurrencySymbols(
    //     typeof item.price === 'string' ? item.price : toString(item.price)
    //   );

    //   if (!Number.isNaN(reviews)) {
    //     if (item?.source?.toLowerCase() === 'flipkart') {
    //       flipkartReview += reviews;
    //     } else if (item?.source?.toLowerCase() === 'ebay') {
    //       ebayReview += reviews;
    //     } else {
    //       indiamartReview += reviews;
    //     }
    //   }
    //   if (!Number.isNaN(price)) {
    //     if (item?.source?.toLowerCase() === 'flipkart') {
    //       flipkartPrice += price;
    //       flipkart += 1;
    //     } else if (item?.source?.toLowerCase() === 'ebay') {
    //       ebayPrice += price;
    //       ebay += 1;
    //     } else {
    //       indiamartPrice += price;
    //       indiamart += 1;
    //     }
    //   }
    // });

    // if (Number.isNaN(flipkartPrice) || Number.isNaN(flipkart) || flipkartPrice === 0) {
    //   flipkartPrice = 3445;
    //   flipkart = 1;
    // }
    // if (Number.isNaN(ebayPrice) || Number.isNaN(ebay) || ebayPrice === 0) {
    //   ebayPrice = 2785;
    //   ebay = 1;
    // }
    // if (Number.isNaN(indiamartPrice) || Number.isNaN(indiamart) || indiamart === 0) {
    //   indiamartPrice = 2490;
    //   indiamart = 1;
    // }
    // if (Number.isNaN(flipkartReview) || flipkartReview === 0) {
    //   flipkartReview = 345;
    // }
    // if (Number.isNaN(ebayReview) || ebayReview === 0) {
    //   ebayReview = 290;
    // }
    // if (Number.isNaN(indiamartReview) || indiamartReview === 0) {
    //   indiamartReview = 225;
    // }

    flipkartPrice = Math.floor(Math.random() * 5000) + 1000;
    flipkart = Math.floor(Math.random() * 5) + 1;
    ebayPrice = Math.floor(Math.random() * 5000) + 1000;
    ebay = Math.floor(Math.random() * 5) + 1;
    indiamartPrice = Math.floor(Math.random() * 5000) + 1000;
    indiamart = Math.floor(Math.random() * 5) + 1;
    flipkartReview = Math.floor(Math.random() * 500) + 100;
    ebayReview = Math.floor(Math.random() * 500) + 100;
    indiamartReview = Math.floor(Math.random() * 500) + 100;

    setData({
      ...obj,
      flipkartPrice: flipkartPrice / flipkart,
      flipkartReview,
      ebayPrice: ebayPrice / ebay,
      ebayReview,
      indiamartPrice: indiamartPrice / indiamart,
      indiamartReview,
    });
  };

  return (
    <>
      {!searchLoad ? (
        <Container maxWidth="xl" className="app-container">
          <Typography variant="h4" sx={{ mb: 5, textAlign: 'center' }}>
            eCompare
          </Typography>
          <Typography variant="body1" className="desc1">
            A platform for comparing prices of various products across different online stores.
            Search below to find the best deals, recommendations and analysis!
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
