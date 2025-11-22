<script lang="ts">
	import { page } from '$app/stores';
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';

	const API_BASE = 'http://127.0.0.1:8000';

	let id = '';
	let track: any = null;
	let loading = true;
	let error: string | null = null;

	$: id = $page.params.id;

	onMount(loadTrack);

	async function loadTrack() {
		try {
			const res = await fetch(`${API_BASE}/tracks/${id}`);
			if (!res.ok) throw new Error('Track not found');
			track = await res.json();
		} catch (err) {
			error = err.message;
		} finally {
			loading = false;
		}
	}

	async function deleteTrack() {
		const res = await fetch(`${API_BASE}/tracks/${id}/delete`, {
			method: 'DELETE'
		});

		if (!res.ok) {
			alert('Failed to delete track.');
			return;
		}

		alert('Track deleted.');
		goto('/tracks');
	}
</script>

<div class="container mt-5" style="max-width: 650px;">
	<div class="card shadow-lg border-0">
		<div class="card-body p-4">

			{#if loading}
				<h4 class="text-center">Loading...</h4>

			{:else if error}
				<h4 class="text-danger text-center">{error}</h4>

			{:else}
				<h2 class="text-danger fw-bold text-center mb-4">
					⚠️ Delete Track
				</h2>

				<p class="text-center mb-4">
					Are you sure you want to permanently delete this track?
				</p>

				<div class="bg-light p-3 rounded mb-4">
					<p><strong>Song:</strong> {track.song_name}</p>
					<p><strong>Artist:</strong> {track.artist}</p>
					<p><strong>Duration:</strong> {track.duration}</p>
				</div>

				<div class="d-flex justify-content-between">
					<button class="btn btn-secondary" on:click={() => goto(`/tracks/${id}`)}>
						Cancel
					</button>

					<button class="btn btn-danger" on:click={deleteTrack}>
						Delete Forever
					</button>
				</div>
			{/if}

		</div>
	</div>
</div>
