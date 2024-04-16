<script setup lang="ts">
export interface ButtonType {
  text: string
  link: string
}

defineProps<{ item: ButtonType }>()
</script>

<template>
  <button class="button">
    <NuxtLink :to="item.link">
      <svg viewBox="0 0 180 60" width="180" height="60">
        <rect x="0" y="0" fill="none" width="180" height="60" />
      </svg>
      <span class="footnote">{{ item.text }}</span>
    </NuxtLink>
  </button>
</template>

<style scoped lang="scss">
.button {
  position: relative;
  width: 180px;
  height: 60px;
  cursor: pointer;
  background: transparent;
  outline: none;
  transition: 1s ease-in-out;

  &:hover {
    transition: 1s ease-in-out;
  }

  &:hover svg {
    stroke-dashoffset: -450;
  }
}

.footnote {
  color: black;
}

svg {
  width: 180px;
  height: 60px;
  position: absolute;
  left: 0;
  top: 0;
  fill: none;
  stroke: $color-secondary;
  stroke-dasharray: 170 480;
  stroke-dashoffset: 150;
  transition: 1s ease-in-out;
}
</style>
