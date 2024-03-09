import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import Stack from '@mui/material/Stack';
import Grid from '@mui/material/Unstable_Grid2';
import axios from 'axios';
import { useState } from 'react';

import './app-styles.css';
import SearchBar from './SearchBar';
import { useNavigate } from 'react-router-dom';
import { useApp } from 'src/context/app-context';
import ProductFilters from 'src/sections/products/product-filters';
import ProductSort from 'src/sections/products/product-sort';
import ProductCard from 'src/sections/products/product-card';

export default function AppView() {
  const { data, setData, dataBlog, setDataBlog } = useApp();
  // const [data, setData] = useState({});
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
          setData(arr);
          setSearchLoad(true);
        }
      })
      .catch((error) => console.log(error));
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
            {data.map((product, index) => (
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
