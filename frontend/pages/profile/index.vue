<script setup lang="ts">
const route = useRoute()
</script>

<template>
  <v-app>
    <h1>
      Profile
    </h1>
    <p>
      Current route: {{ route.path }}
    </p>
    <NuxtLink to="/profile/sadas">
      Перейти на 1 профиль
    </NuxtLink>
  </v-app>
</template>

<style scoped lang="scss">
h1 {
  color: red;
}
</style>
