<template>
  <div class="container">
    <v-app-bar
      scroll-behavior="elevate collapse"
    >
      <template #prepend>
        <v-app-bar-nav-icon />
      </template>

      <v-app-bar-title>Антураж</v-app-bar-title>

      <template #append>
        <v-btn icon="mdi-heart" />

        <v-btn icon="mdi-magnify" />

        <v-btn icon="mdi-dots-vertical" />
      </template>
    </v-app-bar>
  </div>
</template>

<style scoped lang="scss">
.container {
  max-width: 100px;
}
</style>
