<script setup lang="ts">
import { useDisplay } from 'vuetify'

const { sm, xs } = useDisplay()
</script>

<template>
  <HeaderWindow v-if="!sm && !xs" />
  <HeaderMobile v-else />
</template>
