import antfu from '@antfu/eslint-config'

export default antfu({
  rules: {
    'unicorn/filename-case': [
      'error',
      {
        case: 'kebabCase',
      },
    ],
  },
})
