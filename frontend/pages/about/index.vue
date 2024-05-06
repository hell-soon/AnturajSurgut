<script setup lang="ts">
const email = ref()
const password = ref()

function submit() {
  api.auth(email.value, password.value)
}
</script>

<template>
  <h1 class="text-black">
    About
  </h1>
  <v-container>
    <v-text-field v-model="email" label="Почта" variant="underlined" />
    <v-text-field v-model="password" label="Пароль" type="password" variant="underlined" />
    <v-btn @click="submit">
      Вход
    </v-btn>
  </v-container>
</template>

<style scoped lang="scss"></style>
