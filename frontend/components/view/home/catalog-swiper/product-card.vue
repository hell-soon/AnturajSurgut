<script setup lang="ts">
import type { ProductPop } from '~/types/models/product'

defineProps<{ card: ProductPop }>()

const a = ref(false)
</script>

<template>
  <NuxtLink
    :to="`/product/${card.product.id}`" class="card"
    @mouseenter="a = true"
    @mouseleave="a = false"
  >
    <div class="card-img">
      <NuxtImg class="card-img" :src="card.product.image[0].image" alt="card" />
    </div>
    <div class="card-contant">
      <span class="card-contant__title body">
        {{ card.product.name }}
      </span>
      <span class="card-contant__description footnote" v-html="card.product.description" />
      <!-- <Transition name="fade">
        <div v-show="a" class="">
          <span
            v-for="tag in card.product.tags"
            :key="tag.id"
            class="body"
          >
            {{ tag.name }}
          </span>
        </div>
      </Transition> -->
    </div>
  </NuxtLink>
</template>

<style scoped lang="scss">
.fade-enter-active,
.fade-leave-active {
  transition: transform 0.5s ease;
}

.fade-enter-to,
.fade-leave-from {
  transform: translateY(0);
}

.fade-enter-from,
.fade-leave-to {
  transform: translateY(100%);
}

.body,
.footnote {
  color: black;
}
.card {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  border-radius: 10px;
  overflow: hidden;
  transition: box-shadow 0.3s ease-in-out;

  &-img {
    width: 100%;
    height: 350px;
    object-fit: cover;

    img {
      width: 100%;
      height: 100%;
    }
  }

  &-contant {
    border: 1px solid $color-gray;
    border-top: 0;
    border-radius: 0 0 10px 10px;
    width: 100%;
    padding: 20px;
    height: 100%;
    display: flex;
    gap: 15px;
    flex-direction: column;

    &__description {
      overflow: hidden;
      width: 100%;
      height: 100px;
      max-height: 75px;
      display: -webkit-box;
      -webkit-box-orient: vertical;
      -webkit-line-clamp: 3;
      position: relative;
    }
  }

  &:hover {
    box-shadow: 0 0 30px 10px rgba(0, 0, 0, 0.5);

    .card-contant {
      border-color: white;
    }
  }
}
</style>
