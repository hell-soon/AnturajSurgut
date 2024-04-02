<script setup lang="ts">
const route = useRoute()
const a = ref(0)
</script>

<template>
  <div>
    <h1>Nuxt Routing set up successfully!</h1>
    <p>
      Current route: {{ route.path }}, {{ a }}
    </p>
    <NuxtLink to="/">
      Learn more about Nuxt Routing
    </NuxtLink>
  </div>
</template>
