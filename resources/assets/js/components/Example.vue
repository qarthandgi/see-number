<template>
    <main>
        <div class="created-by">by <b>Niles Brandon</b></div>
        <div class="header">ML Digit Recognition</div>
        <div class="paragraph">
            The following exercise uses a Support Vector Machine (SVM) classification algorithm to recognize individually drawn digits into the below JavaScript canvas. Feel free to test the implementation, and parameter tuning of the algorithm by writing some numbers in the box below, and seeing for yourself the accuracy of the tuned algorithm.
        </div>
        <div class="prediction">
            <div class="prediction__header">Your recognized number is:</div>
            <div class="prediction__number">{{predictedNumber}}</div>
        </div>
        <div class="action-buttons">
            <span class="item" @click="clear">Clear</span>
            <!-- <input type="text" v-model="realNumber"> -->
            <span class="item" @click="submit">Submit</span>
        </div>
        <div class="c-container">
            <canvas id="c" width="320" height="320"></canvas>
        </div>
        <transition name="fade">
            <div class="loading-overlay" v-show="predictionLoading"></div>
        </transition>
        <transition name="fade">
            <div class="loader" v-show="predictionLoading">
                <span id="counter"></span>
                <div class="spinner"></div>
            </div>
        </transition>
    </main>
</template>

<script>
    export default {
        data() {
            return {
                canvas: null,
                realNumber: null,
                predictedNumber: null,
                predictionLoading: false
            }
        },
        methods: {
            clear() {
                this.canvas.clear();
            },
            submit() {
                this.predictionLoading = true
                const dataUrl = this.canvas.toDataURL('image/png')
                window.axios.post(location.origin + '/api/number', {
                    'dataUrl': dataUrl,
                    'realNumber': this.realNumber
                }).then(data => {
                    this.predictedNumber = data.data
                    this.predictionLoading = false
                })
            }
        },
        mounted() {
            this.canvas = new window.fabric.Canvas('c', {
                isDrawingMode: true
            })

            this.canvas.freeDrawingBrush.width = 35

        }
    }
</script>