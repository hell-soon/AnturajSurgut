async function fetch<Res>(url: string, options?: any, headers?: any) {
  try {
    const reqUrl = import.meta.env.VITE_API_URL + url

    const customHeaders = { token: useCookie('token').value, ...headers }

    const { data, error, status } = await useFetch(reqUrl, { ...options, headers: customHeaders })

    const result = data.value as Res

    console.log(status.value)

    if (status.value !== 'success') {
      throw createError({
        statusCode: 500,
        statusMessage: reqUrl,
        message: error?.value?.message || '服务器内部错误',
      })
    }
    return result
  }
  catch (err) {
    console.error(err)
    return Promise.reject(err)
  }
}

export function getReq<Res>(url: string, params?: any, headers?: any) {
  return fetch<Res>(url, { method: 'get', params }, headers)
}

export function postReq<Res>(url: string, params?: any, headers?: any) {
  return fetch<Res>(url, { method: 'post', body: params }, headers)
}

export function putReq<Res>(url: string, params?: any, headers?: any) {
  return fetch<Res>(url, { method: 'put', body: params }, headers)
}

export function delReq<Res>(url: string, params?: any, headers?: any) {
  return fetch<Res>(url, { method: 'delete', params }, headers)
}
