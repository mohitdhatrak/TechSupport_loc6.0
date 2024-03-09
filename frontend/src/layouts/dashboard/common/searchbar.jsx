import Input from '@mui/material/Input';
import { styled } from '@mui/material/styles';
import InputAdornment from '@mui/material/InputAdornment';

import { bgBlur } from 'src/theme/css';

import Iconify from 'src/components/iconify';

const HEADER_MOBILE = 64;
const HEADER_DESKTOP = 92;

const StyledSearchbar = styled('div')(({ theme }) => ({
  ...bgBlur({
    color: theme.palette.background.default,
  }),
  width: '100%',
  display: 'flex',
  alignItems: 'center',
  height: HEADER_MOBILE,
  padding: theme.spacing(0, 3),
  boxShadow: theme.customShadows.z8,
  [theme.breakpoints.up('md')]: {
    height: HEADER_DESKTOP,
    padding: theme.spacing(0, 5),
  },
}));

export default function Searchbar() {
  return (
    <StyledSearchbar>
      <Input
        autoFocus
        fullWidth
        disableUnderline
        placeholder="Search…"
        startAdornment={
          <InputAdornment position="start">
            <Iconify
              icon="eva:search-fill"
              sx={{ color: 'text.disabled', width: 20, height: 20 }}
            />
          </InputAdornment>
        }
        sx={{ mr: 1, fontWeight: 'fontWeightBold' }}
      />
    </StyledSearchbar>
  );
}
