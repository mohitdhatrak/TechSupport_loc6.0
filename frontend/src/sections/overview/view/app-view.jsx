import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';
import axios from 'axios';
import { useState } from 'react';

import './app-styles.css';
import SearchBar from './SearchBar';

export default function AppView() {
  const [data, setData] = useState({});
  const [searchValue, setSearchValue] = useState('');

  const handleSearchChange = (event) => {
    setSearchValue(event.target.value);
  };

  const getScrapedData = async () => {
    axios
      .get(`http://127.0.0.1:8000/product/?title=${searchValue}`)
      .then((response) => {
        console.log(response?.data);
        setData(response?.data);
      })
      .catch((error) => console.log(error));
  };

  return (
    <Container maxWidth="xl" className="app-container">
      <Typography variant="h4" sx={{ mb: 5, textAlign: 'center' }}>
        eCompare
      </Typography>
      <Typography variant="body1" className="desc1">
        A platform for comparing prices of various products across different online stores. Search
        below to find the best deals, recommendations and analysis!
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
  );
}
