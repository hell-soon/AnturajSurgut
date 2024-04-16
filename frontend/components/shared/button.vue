<script setup lang="ts">
export interface ButtonType {
  text: string
  link: string
}

defineProps<{ item: ButtonType }>()
</script>

<template>
  <div class="center">
    <button class="button">
      <NuxtLink :to="item.link">
        <svg width="180px" height="60px" viewBox="0 0 180 60" class="border">
          <polyline points="180,1 180,60 1,60 1,1 180,1" class="bg-line" />
          <polyline points="180,1 180,60 1,60 1,1 180,1" class="hl-line" />
        </svg>
        <span class="footnote">{{ item.text }}</span>
      </NuxtLink>
    </button>
  </div>
</template>

<style scoped lang="scss">
.button {
  width: 180px;
  height: 60px;
  cursor: pointer;
  background: transparent;
  border: 1px solid #91c9ff;
  outline: none;
  transition: 1s ease-in-out;
}

.center {
  width: 200px;
  height: 60px;
  position: relative;
}

svg {
  position: absolute;
  left: 0;
  top: 0;
  fill: none;
  stroke: #fff;
  stroke-dasharray: 150 480;
  stroke-dashoffset: 150;
  transition: 1s ease-in-out;
}

.button:hover {
  transition: 1s ease-in-out;
  background: #4f95da;
}

.button:hover svg {
  stroke-dashoffset: -480;
}
</style>
