<script setup lang="ts">

</script>

<template>
  <v-app>
    <h1>
      Profile 1
    </h1>
    <p>
      Current route: {{ $route.path }}
    </p>
    <NuxtLink to="/">
      Вернуться на главную
    </NuxtLink>
  </v-app>
</template>

<style scoped lang="scss">
h1 {
  color: red;
}
</style>
