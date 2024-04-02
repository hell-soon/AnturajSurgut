<script setup lang="ts">
const route = useRoute()
</script>

<template>
  <v-app>
    <h1 class="text-center">
      Сургут епта!
    </h1>
    <p>
      Current route: {{ route.path }}
    </p>
    <NuxtLink to="/about">
      Перейти на 404
    </NuxtLink>
  </v-app>
</template>

<style lang="scss">
h1 {
  color: red;
}
</style>
