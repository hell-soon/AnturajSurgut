interface ListItem {
  name: string
  link?: string
  badge?: boolean
}

const main: ListItem[] = [
  {
    name: 'Товары',
    link: '/product',
  },
  {
    name: 'Услуги',
    link: '/services',
  },
  {
    name: 'Оптовикам',
    link: '/wholesalers',
  },
  {
    name: 'О нас',
    link: '/about',
  },
]

const second: ListItem[] = [
  {
    name: 'profile',
    link: '/profile',
  },
  {
    name: 'search',
  },
  {
    name: 'shopping-cart',
    badge: true,
  },
]

export default { main, second }
