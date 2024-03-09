import Container from '@mui/material/Container';
import Typography from '@mui/material/Typography';

import './app-styles.css';
import SearchBar from './SearchBar';

export default function AppView() {
  return (
    <>
      <Container maxWidth="xl">
        <Typography variant="h4" sx={{ mb: 5 }}>
          Hi, Welcome to eCompare 👋
        </Typography>
        <Typography variant="body1" className="desc1">
          A platform for comparing prices of various products across different online stores. Search
          below to find the best deals, recommendations and analysis!
        </Typography>
        <Typography variant="body1" className="desc2">
          Search for <span className="animated" />
        </Typography>
        <SearchBar label="Search products..." variant="outlined" />
      </Container>
    </>
  );
}
