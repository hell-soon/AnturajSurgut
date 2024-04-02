import antfu from '@antfu/eslint-config'

export default antfu({
  formatters: true,
  rules: {
    'unicorn/filename-case': [
      'error',
      {
        case: 'kebabCase',
      },
    ],
  },
})
