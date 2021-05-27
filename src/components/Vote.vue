<template lang="html">
  <div class="vote">
    <svg @click="upVote" :class="{ active: votedUp }" fill="#000000" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
      <path d="M7.41 15.41L12 10.83l4.59 4.58L18 14l-6-6-6 6z"/>
      <path d="M0 0h24v24H0z" fill="none"/>
    </svg>
    <p>{{ voting }}</p>
    <svg @click="downVote" :class="{ active: votedDown }" fill="#000000" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
      <path d="M7.41 7.84L12 12.42l4.59-4.58L18 9.25l-6 6-6-6z"/>
      <path d="M0-.75h24v24H0z" fill="none"/>
    </svg>
  </div>
</template>

<script>
import store from '@/store/index'
import PostsService from '@/services/PostsService'

export default {
    name: 'vote',

    props: ['upvotes', 'downvotes', 'postId'],
    data(){
        return {
            upVoteData: this.upvotes,
            downVoteData: this.downvotes,
        }

    },

    methods: {
        upVote() {
            PostsService.upVote(this.postId)
                .then(response => {
                    this.upVoteData = response.data.upvotes
                    this.downVoteData = response.data.downvotes
                })
                .catch(e => {
                    this.$emit('error', e.response.data.error)
                })
        },

        downVote() {
            PostsService.downVote(this.postId)
                .then(response => {
                    this.upVoteData = response.data.upvotes
                    this.downVoteData = response.data.downvotes
                })
                .catch(e => {
                    this.$emit('error', e.response.data.error)
                })
        }
    },

    computed: {
        voting() {
            return this.upVoteData.length - this.downVoteData.length
        },

        votedUp() {
            if (!store.state.isUserLoggedIn) {
                return false
            }

            for (var i in this.upVoteData) {
                if (this.upVoteData[i].username == store.state.user.username) {
                    return true
                }
            }
            return false
        },

        votedDown() {
            if (!store.state.isUserLoggedIn) {
                return false
            }

            for (var i in this.downVoteData) {
                if (this.downVoteData[i].username == store.state.user.username) {
                    return true
                }
            }
            return false
        }
    },
}
</script>

<style lang="css">
.vote {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 20px;
}

.vote p {
    margin: 10px 0;
}

.vote svg.active {
    fill: red;
}

.vote svg:hover {
    fill: rgb(27, 122, 249);
    cursor: pointer;
}
</style>
