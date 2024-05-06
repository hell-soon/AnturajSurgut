<template>
  <v-dialog max-width="500" transition="slide-x-reverse-transition" scrollable>
    <template #activator="{ props: activatorProps }">
      <v-btn icon="" v-bind="activatorProps" variant="plain">
        <slot name="activator" />
      </v-btn>
    </template>

    <template #default="{ isActive }">
      <v-card title="Dialog">
        <v-card-text>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
        </v-card-text>

        <v-card-actions>
          <v-spacer />

          <v-btn
            text="Close Dialog"
            @click="isActive.value = false"
          />
        </v-card-actions>
      </v-card>
    </template>
  </v-dialog>
</template>

<style scoped lang="scss">
.v-dialog {
  :deep(.v-overlay__content) {
    margin: $cover-12;
    height: 100%;
    right: 0;
  }

  :deep(.v-card) {
    height: 100%;
  }
}
</style>
