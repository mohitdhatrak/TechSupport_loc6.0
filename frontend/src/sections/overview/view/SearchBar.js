import { styled } from '@mui/material/styles';
import TextField from '@mui/material/TextField';

const SearchBar = styled(TextField)({
  borderRadius: '1000px',
  width: '40rem',
  maxWidth: '80vw',
  margin: '0 auto',
  display: 'flex',
  justifyContent: 'center',
  marginTop: '5vh',
  fontSize: '5rem',
});

export default SearchBar;
