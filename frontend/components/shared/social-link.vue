<script setup lang="ts">
const props = defineProps<{ info: string, params: 'tel' | 'mailto' }>()

const link = `${props.params}:${props.info}`
</script>

<template>
  <a :href="link" class="h3">{{ info }}</a>
</template>
