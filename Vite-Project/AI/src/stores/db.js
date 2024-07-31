import Dexie from 'dexie';
import { useObservable } from "@vueuse/rxjs";
import * as _ from 'lodash'

export const db = new Dexie('myDatabase');

db.version(1).stores({
  xray: 'id, title, src, scanResult, suggestion',
  pathological: 'id, title, src, scanResult, suggestion',
  electrocardiograph: 'id, title, src, scanResult, suggestion',
});


export const orderBy = (collection, iteratees = (data) => data?.title, order=['desc']) => {
    return _.orderBy(collection, iteratees, order)
}


export const addXrayDb = async (data) => {
    const res = await db.xray.add(data)
    return res
}
export const queryXrayDb = () => {
    return new Promise((resolve) => {
        const list = useObservable(
            Dexie.liveQuery(() => db.xray.toArray())
        )
        setTimeout(() => {
            resolve(orderBy(list.value))
        })
    })
}
export const addPathologicalDb = async (data) => {
    const res = await db.pathological.add(data)
}
export const queryPathologicalDb = () => {
    return new Promise((resolve) => {
      const list = useObservable(
        Dexie.liveQuery(() => db.pathological.toArray())
      )
      setTimeout(() => {
        resolve(orderBy(list.value))
      })
    })
}
export const addElectrocardiographDb = async (data) => {
    const res = await db.electrocardiograph.add(data)
}
export const queryElectrocardiographDb = () => {
    return new Promise((resolve) => {
      const list = useObservable(
        Dexie.liveQuery(() => db.electrocardiograph.toArray())
      )
      setTimeout(() => {
        resolve(orderBy(list.value))
      })
    })
}