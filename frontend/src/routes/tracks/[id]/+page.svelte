<script lang="ts">
	import { page } from '$app/stores';
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';

	const API_BASE = 'http://127.0.0.1:8000';

	let id: string | undefined;
	let track: any = null;
	let loading = true;
	let error: string | null = null;

	// get URL param
	$: id = $page.params.id;

	onMount(() => {
		loadTrack();
	});

	async function loadTrack() {
		error = null;
		loading = true;

		try {
			const res = await fetch(`${API_BASE}/tracks/${id}`);

			if (!res.ok) {
				throw new Error(`Failed to load track (${res.status})`);
			}

			track = await res.json();
		} catch (err) {
			error = err instanceof Error ? err.message : 'Unknown error';
		} finally {
			loading = false;
		}
	}
</script>

<h1>Track Details</h1>

{#if loading}
	<p>Loading...</p>
{:else if error}
	<p style="color: red">{error}</p>
{:else}
	<div class="track-card">
		<h2>{track.song_name}</h2>
		<p><strong>Artist:</strong> {track.artist}</p>
		<p><strong>Duration:</strong> {track.duration}</p>
		<p><strong>ID:</strong> {track.id}</p>
		<button class="btn btn-success" on:click={() => goto(`/tracks/${id}/edit`)}>Edit</button>
		<button class="btn btn-danger" on:click={() => goto(`/tracks/${id}/delete`)}>Delete</button>
		<a href="/tracks">View All Tracks</a>
	</div>
{/if}

<style>
	.track-card {
		padding: 1rem;
		border: 1px solid #ddd;
		border-radius: 8px;
		max-width: 450px;
	}

</style>
