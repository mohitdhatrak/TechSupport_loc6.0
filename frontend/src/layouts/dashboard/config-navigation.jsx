import SvgColor from 'src/components/svg-color';

const icon = (name) => (
  <SvgColor src={`/assets/icons/navbar/${name}.svg`} sx={{ width: 1, height: 1 }} />
);

const navConfig = [
  {
    title: 'search',
    path: '/',
    icon: icon('ic_analytics'),
  },
  // {
  //   title: 'compare',
  //   path: '/products',
  //   icon: icon('ic_cart'),
  // },
  {
    title: 'analyze',
    path: '/analyze',
    icon: icon('ic_blog'),
  },
  {
    title: 'login',
    path: '/login',
    icon: icon('ic_lock'),
  },
];

export default navConfig;
